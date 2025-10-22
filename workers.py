from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .repositories import SensorRepository


# Instância global do agendador
scheduler = AsyncIOScheduler()


async def batch_aggregate():
    """
    Job de exemplo: agrega as leituras recentes do sensor.
    Pode salvar resultados em outra coleção, gerar CSV ou enviar a outro sistema.
    """
    try:
        repo = SensorRepository()
        data = await repo.find_recent(limit=1000)
        print(f"[Batch Aggregate] Processadas {len(data)} leituras.")
        # Aqui você pode:
        # - calcular médias, máximos, mínimos
        # - salvar resultados em outra coleção
        # - exportar CSV
    except Exception as e:
        print("[Batch Aggregate] Erro:", e)


def start_scheduler():
    """
    Inicia o agendador de tarefas periódicas.
    """
    scheduler.add_job(
        batch_aggregate,
        trigger='interval',
        minutes=5,
        id='batch_aggregate',
        coalesce=True,  # evita rodar múltiplas execuções simultâneas
        misfire_grace_time=30  # tolera atrasos leves
    )
    scheduler.start()
    print("[Scheduler] Iniciado: job batch_aggregate a cada 5 minutos.")
