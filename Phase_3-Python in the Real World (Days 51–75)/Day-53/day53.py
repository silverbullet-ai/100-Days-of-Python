# Day 53 — Logging vs Print & Professional Debugging

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

print("PROGRAM STARTED (using print)\n", flush = 'True')


def divide_numbers(a: float, b: float) -> float:
    logger.info("Attempting division")

    if b == 0:
        logger.error("Division by zero attempted")
        raise ValueError("Cannot divide by zero")

    result = a / b
    logger.debug("Division successful")

    return result


def main():
    logger.info("Program execution started")

    try:
        value = divide_numbers(10, 2)
        logger.info(f"Division result: {value}")
    except ValueError as error:
        logger.warning(f"Handled error: {error}")

    logger.info("Program execution finished")


if __name__ == "__main__":
    main()

print("\nDay 53 completed successfully!")
