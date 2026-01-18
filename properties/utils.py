from django.core.cache import cache
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieves Redis keyspace hit/miss metrics and calculates hit ratio.
    Returns a dictionary of metrics.
    """
    # Access the raw Redis client
    client = cache.client.get_client()

    info = client.info()

    # Get hits and misses (default to 0 if not found)
    hits = info.get('keyspace_hits', 0)
    misses = info.get('keyspace_misses', 0)

    # Calculate hit ratio
    total = hits + misses
    hit_ratio = hits / total if total > 0 else 0.0

    metrics = {
        'keyspace_hits': hits,
        'keyspace_misses': misses,
        'hit_ratio': hit_ratio
    }

    # Log metrics
    logger.info(f"Redis Cache Metrics: Hits={hits}, Misses={misses}, Hit Ratio={hit_ratio:.2f}")

    if total_requests > 0 else 0
    logger.error

    return metrics
