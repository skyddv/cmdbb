from django.db import models


class Schema(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, unique=True, null=False)
    display = models.CharField(max_length=45, unique=True, null=False)
    deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.name


class cc(models.Model):
    question = models.ForeignKey(Schema, on_delete=models.CASCADE)
    deleted = models.CharField(max_length=45)

    def __str__(self):
            return self.deleted


#     fields = relationship('Field', back_populates='schema', foreign_keys='[Field.schema_id]')
#
#
# class Field(models.Model):
#     __tablename__ = 'field'
#
#     TYPE_INT = 0
#     TYPE_FLOAT = 1
#     TYPE_STRING = 2
#     TYPE_DATETIME = 3
#     TYPE_IP = 4
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     schema_id = Column(Integer, ForeignKey('schema.id'), nullable=False)
#     name = Column(String(45), unique=True, nullable=False)
#     display = Column(String(45), unique=True, nullable=False)
#     type = Column(Integer, nullable=False, default=TYPE_STRING)
#     required = Column(Boolean, nullable=False, default=True)
#     multi = Column(Boolean, nullable=False, default=False)
#     unique = Column(Boolean, nullable=False, default=False)
#     default = Column(BLOB, nullable=True)
#     deleted = Column(Boolean, nullable=False, default=False)
#
#     schema = relationship('Schema', back_populates='fields', foreign_keys=[schema_id])
#     histories = relationship('FieldHistory', back_populates='field', foreign_keys=['FieldHistory.field_id'])
#
#     __table_args__ = (UniqueConstraint(schema_id, name, name='uq_field_schema_name'),
#                       UniqueConstraint(schema_id, display, name='uq_field_schema_display'))
#
#
# class FieldHistory(models.Model):
#     __tablename__ = 'field_history'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     schema_id = Column(Integer, ForeignKey('schema.id'), nullable=False)
#     name = Column(String(45), unique=True, nullable=False)
#     display = Column(String(45), unique=True, nullable=False)
#     type = Column(Integer, nullable=False, default=Field.TYPE_STRING)
#     required = Column(Boolean, nullable=False, default=True)
#     multi = Column(Boolean, nullable=False, default=False)
#     unique = Column(Boolean, nullable=False, default=False)
#     default = Column(BLOB, nullable=True)
#     deleted = Column(Boolean, nullable=False, default=False)
#
#     field_id = Column(Integer, ForeignKey('field.id'), nullable=False)
#     timestamp = Column(DateTime, nullable=False, index=True)
#
#     field = relationship('Field', back_populates='histories', foreign_keys=[field_id])
#
#
# class Relationship(models.Model):
#     __tablename__ = 'relationship'
#
#     source_id = Column(Integer, ForeignKey('field.id'), primary_key=True)
#     target_id = Column(Integer, ForeignKey('field.id'), primary_key=True)
#
#
# class Entity(models.Model):
#     __tablename__ = 'entity'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     schema_id = Column(Integer, ForeignKey('schema.id'), nullable=False)
#
#     schema = relationship('Schema', foreign_keys=[schema_id])
#     values = relationship('Value', foreign_keys='[Value.entity_id]')
#
#
# class Value(models.Model):
#     __tablename__ = 'value'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     entity_id = Column(Integer, ForeignKey('entity.id'), nullable=False)
#     field_id = Column(Integer, ForeignKey('field.id'), nullable=False)
#     value = Column(BLOB, nullable=False, index=True)
#
#     field = relationship('Field', foreign_keys=[field_id])
#
#
# class ValueHistory(models.Model):
#     __tablename__ = 'value_history'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     entity_id = Column(Integer, ForeignKey('entity.id'), nullable=False)
#     field_id = Column(Integer, ForeignKey('field.id'), nullable=False)
#     value = Column(BLOB, nullable=False, index=True)
#
#     deleted = Column(Boolean, nullable=False, default=False)
#     timestamp = Column(DateTime, nullable=False, index=True)
