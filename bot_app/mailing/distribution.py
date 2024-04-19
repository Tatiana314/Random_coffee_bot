from typing import Iterable, List, Dict

from sqlalchemy.ext.asyncio import AsyncSession

from bot_app.database.models import User


def get_unique_pairs(users: Iterable) -> List[tuple]:
    """Making pairs."""
    return list(
        zip(users[:len(users) // 2], reversed(users[len(users) // 2:]))
    )


async def distribute_pairs(session: AsyncSession) -> Dict:
    """Distributes pairs of users."""
    actives = await User.get_all_activated(session)
    if len(actives) <= 1:
        return {}
    if len(actives) > 1:
        await User.move_to_end(actives[0], session)
    if len(actives) % 2 == 0:
        return {'pairs': get_unique_pairs(actives)}
    no_pair = actives.pop(len(actives) // 2)
    await User.move_to_end(no_pair, session)
    return {'pairs': get_unique_pairs(actives), 'no_pair': no_pair}
