"""Initial schema

Revision ID: 001
Revises: 
Create Date: 2025-11-14 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create usuarios table
    op.create_table('usuarios',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nombre', sa.String(length=200), nullable=False),
        sa.Column('email', sa.String(length=200), nullable=False),
        sa.Column('hash_password', sa.String(length=255), nullable=False),
        sa.Column('rol', sa.String(length=50), nullable=False),
        sa.Column('estado', sa.String(length=50), nullable=False),
        sa.Column('telefono', sa.String(length=50), nullable=True),
        sa.Column('mfa_secret', sa.String(length=100), nullable=True),
        sa.Column('mfa_enabled', sa.Boolean(), nullable=True),
        sa.Column('creado_en', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('actualizado_en', sa.DateTime(timezone=True), nullable=True),
        sa.Column('ultimo_acceso', sa.DateTime(timezone=True), nullable=True),
        sa.Column('notas', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usuarios_id'), 'usuarios', ['id'], unique=False)
    op.create_index(op.f('ix_usuarios_email'), 'usuarios', ['email'], unique=True)
    op.create_index(op.f('ix_usuarios_rol'), 'usuarios', ['rol'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_usuarios_rol'), table_name='usuarios')
    op.drop_index(op.f('ix_usuarios_email'), table_name='usuarios')
    op.drop_index(op.f('ix_usuarios_id'), table_name='usuarios')
    op.drop_table('usuarios')


