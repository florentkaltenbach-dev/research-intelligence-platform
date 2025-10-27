"""
Custom middleware for the Research Intelligence Platform.
"""
import time
import logging
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware to log all HTTP requests and responses."""

    async def dispatch(self, request: Request, call_next):
        """
        Log request and response details.

        Args:
            request: The incoming request
            call_next: The next middleware/route handler
        """
        # Start timer
        start_time = time.time()

        # Extract request info
        client_ip = request.client.host if request.client else "unknown"
        method = request.method
        url = str(request.url)

        # Log request
        logger.info(f"Request: {method} {url} from {client_ip}")

        try:
            # Process request
            response: Response = await call_next(request)

            # Calculate duration
            duration = time.time() - start_time

            # Log response
            logger.info(
                f"Response: {method} {url} - "
                f"Status: {response.status_code} - "
                f"Duration: {duration:.3f}s"
            )

            # Add custom headers
            response.headers["X-Process-Time"] = str(duration)

            return response

        except Exception as e:
            # Log error
            duration = time.time() - start_time
            logger.error(
                f"Error: {method} {url} - "
                f"Error: {str(e)} - "
                f"Duration: {duration:.3f}s",
                exc_info=True
            )
            raise


class UsageAnalyticsMiddleware(BaseHTTPMiddleware):
    """Middleware to track usage analytics."""

    def __init__(self, app: ASGIApp):
        super().__init__(app)
        self.request_count = 0
        self.endpoint_stats = {}

    async def dispatch(self, request: Request, call_next):
        """
        Track usage statistics.

        Args:
            request: The incoming request
            call_next: The next middleware/route handler
        """
        # Increment counter
        self.request_count += 1

        # Track endpoint
        endpoint = f"{request.method} {request.url.path}"
        self.endpoint_stats[endpoint] = self.endpoint_stats.get(endpoint, 0) + 1

        # Process request
        response = await call_next(request)

        # Add analytics header
        response.headers["X-Request-Count"] = str(self.request_count)

        return response
