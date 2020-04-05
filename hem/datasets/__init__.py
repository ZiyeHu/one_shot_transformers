from hem.datasets.savers.trajectory import Trajectory


def get_dataset(name):
    if name == 'something something':
        from .something_dataset import SomethingSomething
        return SomethingSomething
    elif name == 'agent teacher':
        from .agent_teacher_dataset import AgentTeacherDataset
        return AgentTeacherDataset
    elif name == 'paired agent teacher':
        from .agent_teacher_dataset import PairedAgentTeacherDataset
        return PairedAgentTeacherDataset
    elif name == 'agent':
        from .agent_dataset import AgentDemonstrations
        return AgentDemonstrations
    raise NotImplementedError


def get_validation_batch(loader, batch_size=8):
    pass
