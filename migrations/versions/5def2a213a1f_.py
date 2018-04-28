"""empty message

Revision ID: 5def2a213a1f
Revises: b76b9de5fe31
Create Date: 2018-04-28 22:57:06.584644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5def2a213a1f'
down_revision = 'b76b9de5fe31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'follows_follower_id_key', 'follows', type_='unique')
    op.drop_constraint(u'follows_user_id_key', 'follows', type_='unique')
    op.drop_constraint(u'likes_post_id_key', 'likes', type_='unique')
    op.drop_constraint(u'likes_user_id_key', 'likes', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(u'likes_user_id_key', 'likes', ['user_id'])
    op.create_unique_constraint(u'likes_post_id_key', 'likes', ['post_id'])
    op.create_unique_constraint(u'follows_user_id_key', 'follows', ['user_id'])
    op.create_unique_constraint(u'follows_follower_id_key', 'follows', ['follower_id'])
    # ### end Alembic commands ###
