"""
Sentry integration for error tracking and monitoring (optional).
"""
import logging
from typing import Optional

logger = logging.getLogger(__name__)


def init_sentry(
    dsn: Optional[str] = None,
    environment: str = "development",
    enable_tracing: bool = True,
    traces_sample_rate: float = 0.1
) -> bool:
    """
    Initialize Sentry for error tracking and performance monitoring.

    Args:
        dsn: Sentry DSN (Data Source Name). If None, Sentry will not be initialized.
        environment: Environment name (development, staging, production)
        enable_tracing: Whether to enable performance tracing
        traces_sample_rate: Sampling rate for performance traces (0.0 to 1.0)

    Returns:
        True if Sentry was initialized successfully, False otherwise
    """
    if not dsn:
        logger.info("Sentry DSN not provided - error tracking disabled")
        return False

    try:
        import sentry_sdk
        from sentry_sdk.integrations.fastapi import FastApiIntegration
        from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
        from sentry_sdk.integrations.logging import LoggingIntegration

        # Configure logging integration
        logging_integration = LoggingIntegration(
            level=logging.INFO,  # Capture info and above as breadcrumbs
            event_level=logging.ERROR  # Send errors as events
        )

        sentry_sdk.init(
            dsn=dsn,
            environment=environment,
            integrations=[
                FastApiIntegration(),
                SqlalchemyIntegration(),
                logging_integration
            ],
            traces_sample_rate=traces_sample_rate if enable_tracing else 0.0,
            send_default_pii=False,  # Don't send personally identifiable information
            attach_stacktrace=True,
            # Release can be set to git commit hash in production
            # release="research-platform@1.0.0"
        )

        logger.info(f"Sentry initialized successfully for environment: {environment}")
        return True

    except ImportError:
        logger.warning(
            "Sentry SDK not installed. Install with: pip install sentry-sdk[fastapi]"
        )
        return False
    except Exception as e:
        logger.error(f"Failed to initialize Sentry: {e}")
        return False


def capture_exception(error: Exception, context: dict = None) -> None:
    """
    Manually capture an exception to Sentry with optional context.

    Args:
        error: The exception to capture
        context: Additional context to attach to the error
    """
    try:
        import sentry_sdk

        if context:
            with sentry_sdk.push_scope() as scope:
                for key, value in context.items():
                    scope.set_context(key, value)
                sentry_sdk.capture_exception(error)
        else:
            sentry_sdk.capture_exception(error)

    except ImportError:
        # Sentry not installed, just log
        logger.error(f"Exception occurred: {error}", exc_info=True)


def capture_message(message: str, level: str = "info", context: dict = None) -> None:
    """
    Manually capture a message to Sentry.

    Args:
        message: The message to capture
        level: Severity level (debug, info, warning, error, fatal)
        context: Additional context to attach
    """
    try:
        import sentry_sdk

        if context:
            with sentry_sdk.push_scope() as scope:
                for key, value in context.items():
                    scope.set_context(key, value)
                sentry_sdk.capture_message(message, level)
        else:
            sentry_sdk.capture_message(message, level)

    except ImportError:
        # Sentry not installed, just log
        log_level = getattr(logging, level.upper(), logging.INFO)
        logger.log(log_level, message)


def set_user_context(user_id: str, email: str = None, username: str = None) -> None:
    """
    Set user context for Sentry error tracking.

    Args:
        user_id: User identifier
        email: User email (optional)
        username: Username (optional)
    """
    try:
        import sentry_sdk

        sentry_sdk.set_user({
            "id": user_id,
            "email": email,
            "username": username
        })
    except ImportError:
        pass


def add_breadcrumb(message: str, category: str = "default", level: str = "info", data: dict = None) -> None:
    """
    Add a breadcrumb to track events leading up to an error.

    Args:
        message: Breadcrumb message
        category: Category (e.g., "query", "request", "auth")
        level: Severity level
        data: Additional data
    """
    try:
        import sentry_sdk

        sentry_sdk.add_breadcrumb(
            message=message,
            category=category,
            level=level,
            data=data or {}
        )
    except ImportError:
        pass
