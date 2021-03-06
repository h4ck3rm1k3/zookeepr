"""
 * SET NOT NULL for person_id on travel

Revision ID: 4cecbeb21fbf
Revises: 209af87cb54
Create Date: 2012-09-04 16:51:36.136908

"""

# revision identifiers, used by Alembic.
revision = '4cecbeb21fbf'
down_revision = '2742a682f066'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('travel', u'person_id', 
               existing_type=sa.INTEGER(), 
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('travel', u'person_id', 
               existing_type=sa.INTEGER(), 
               nullable=True)
    ### end Alembic commands ###
