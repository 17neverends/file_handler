import logging
import psutil
from config import get_logger

logger: logging.Logger = get_logger("network.log")


def log_network_activity():
    logged_connections = set()

    while True:
        connections = psutil.net_connections(kind='inet')

        for conn in connections:
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
            status = conn.status
            process = psutil.Process(conn.pid).name() if conn.pid else "N/A"

            connection_info = (laddr, raddr, status, process)

            if connection_info not in logged_connections:
                logged_connections.add(connection_info)
                logger.info(f"Процесс: {process} | Локальный адрес: {laddr} | Удаленный адрес: {raddr} | Статус: {status}")


if __name__ == "__main__":
    try:
        log_network_activity()
    except KeyboardInterrupt:
        logger.info("Завершение работы скрипта.")
