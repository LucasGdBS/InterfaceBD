"""First_version

Revision ID: 5803096c35eb
Revises: 
Create Date: 2023-12-02 20:39:23.766031

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5803096c35eb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('specie_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('animals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('surname', sa.String(length=50), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=1), nullable=False),
    sa.Column('specie_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['specie_id'], ['species.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('animals')
    op.drop_table('species')
    # ### end Alembic commands ###