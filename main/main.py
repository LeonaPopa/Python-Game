from repository.repository import Repository
from service.service import Service
from ui.console import Console
from validators.Validators import Validators

dimension = 7 + 1
dimension = int(dimension)
validator = Validators()
repository = Repository(dimension)
service = Service(repository, dimension)
console = Console(service, dimension, validator)
with_gui = True
console.run_console(with_gui)
