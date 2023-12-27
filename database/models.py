# database/model.py
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# Declaration of all database tables

class Domains(Base):
    __tablename__ = 'Domains'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)

    sites = relationship("Sites", back_populates="domain")


class Sites(Base):
    __tablename__ = 'Sites'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode(255), nullable=False)

    links = relationship('Links', back_populates='site')

    domain_id = Column(Integer, ForeignKey('Domains.id'), nullable=False)
    domain = relationship('Domains', back_populates='sites')


class ScrapingDate(Base):
    __tablename__ = 'ScrapingDate'
    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime, default=datetime.now)

    links = relationship('Links', back_populates='datetime')


class Links(Base):
    __tablename__ = 'Links'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Unicode pour supporter les emojis
    name = Column(Unicode(512, collation='utf8mb4_unicode_ci'))
    url = Column(String(1024), nullable=False)

    date_id = Column(Integer, ForeignKey('ScrapingDate.id'))
    datetime = relationship('ScrapingDate', back_populates='links')

    site_id = Column(Integer, ForeignKey('Sites.id'))
    site = relationship('Sites', back_populates='links')
