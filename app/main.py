
import logging
import sys

async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())