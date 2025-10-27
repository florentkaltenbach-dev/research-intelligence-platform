"""
Redis caching utilities for the Research Intelligence Platform.
"""
import redis
import json
import logging
from typing import Optional, Any
from functools import wraps
from backend.config import settings

logger = logging.getLogger(__name__)


class CacheManager:
    """Manages Redis caching operations."""

    def __init__(self):
        """Initialize Redis connection."""
        self.redis_client: Optional[redis.Redis] = None
        self.enabled = False

        if settings.redis_url:
            try:
                self.redis_client = redis.from_url(
                    settings.redis_url,
                    decode_responses=True,
                    socket_timeout=5,
                    socket_connect_timeout=5
                )
                # Test connection
                self.redis_client.ping()
                self.enabled = True
                logger.info(f"Redis cache enabled: {settings.redis_url}")
            except (redis.ConnectionError, redis.TimeoutError) as e:
                logger.warning(f"Redis connection failed, caching disabled: {e}")
                self.redis_client = None
                self.enabled = False
        else:
            logger.info("Redis URL not configured, caching disabled")

    def get(self, key: str) -> Optional[Any]:
        """
        Get value from cache.

        Args:
            key: Cache key

        Returns:
            Cached value or None if not found
        """
        if not self.enabled or not self.redis_client:
            return None

        try:
            value = self.redis_client.get(key)
            if value:
                logger.debug(f"Cache hit: {key}")
                return json.loads(value)
            logger.debug(f"Cache miss: {key}")
            return None
        except Exception as e:
            logger.error(f"Cache get error for key {key}: {e}")
            return None

    def set(self, key: str, value: Any, ttl: int = 300):
        """
        Set value in cache.

        Args:
            key: Cache key
            value: Value to cache
            ttl: Time to live in seconds (default 5 minutes)
        """
        if not self.enabled or not self.redis_client:
            return

        try:
            self.redis_client.setex(
                key,
                ttl,
                json.dumps(value, default=str)  # default=str handles datetime
            )
            logger.debug(f"Cache set: {key} (TTL: {ttl}s)")
        except Exception as e:
            logger.error(f"Cache set error for key {key}: {e}")

    def delete(self, key: str):
        """
        Delete value from cache.

        Args:
            key: Cache key
        """
        if not self.enabled or not self.redis_client:
            return

        try:
            self.redis_client.delete(key)
            logger.debug(f"Cache deleted: {key}")
        except Exception as e:
            logger.error(f"Cache delete error for key {key}: {e}")

    def delete_pattern(self, pattern: str):
        """
        Delete all keys matching a pattern.

        Args:
            pattern: Key pattern (e.g., "events:*")
        """
        if not self.enabled or not self.redis_client:
            return

        try:
            keys = self.redis_client.keys(pattern)
            if keys:
                self.redis_client.delete(*keys)
                logger.debug(f"Cache pattern deleted: {pattern} ({len(keys)} keys)")
        except Exception as e:
            logger.error(f"Cache delete pattern error for {pattern}: {e}")

    def clear(self):
        """Clear all cache."""
        if not self.enabled or not self.redis_client:
            return

        try:
            self.redis_client.flushdb()
            logger.info("Cache cleared")
        except Exception as e:
            logger.error(f"Cache clear error: {e}")


# Global cache manager instance
cache = CacheManager()


def cached(key_prefix: str, ttl: int = 300):
    """
    Decorator to cache function results.

    Args:
        key_prefix: Prefix for cache key
        ttl: Time to live in seconds

    Usage:
        @cached("events:list", ttl=600)
        async def get_events():
            # ... expensive operation
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Generate cache key from function name and arguments
            cache_key = f"{key_prefix}:{func.__name__}"

            # Try to get from cache
            cached_value = cache.get(cache_key)
            if cached_value is not None:
                return cached_value

            # Execute function
            result = await func(*args, **kwargs)

            # Cache result
            cache.set(cache_key, result, ttl)

            return result

        return wrapper
    return decorator


def invalidate_cache(*patterns: str):
    """
    Invalidate cache for given patterns.

    Args:
        patterns: Cache key patterns to invalidate

    Usage:
        invalidate_cache("events:*", "stats:*")
    """
    for pattern in patterns:
        cache.delete_pattern(pattern)
