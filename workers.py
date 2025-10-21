# exemplo: tarefas de retry, agregação batch, exportação
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .repositories import SensorRepository


# Agendador simples (se quiser agregar ou exportar periodicamente)


scheduler = AsyncIOScheduler()


async def batch_aggregate():
repo = SensorRepository()
data = await repo.find_recent(limit=1000)
# executar agregações / salvar em outra coleção / exportar CSV
print("Batch aggregate: got", len(data))


def start_scheduler():
scheduler.add_job(batch_aggregate, 'interval', minutes=5)
scheduler.start()