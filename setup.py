#!/usr/bin/env python3
"""
Setup for the slackpile project
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name="slackpile",
      packages=["slack_backup"],
      version="0.4.4",
      description="Store Slack Conversations in Local DB",
      author="Ayush Pareek",
      author_email="ayush.original@gmail.com",
      url="https://github.com/ayushoriginal/slackpile",
      download_url="https://github.com/ayushoriginal/slackpile",
      keywords=["log", "store", "conversations", "slack"],
      install_requires=["sqlalchemy", "slackclient"],
      scripts=["scripts/slack-backup"],
      classifiers=["Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.4",
                   "Development Status :: 3 - Alpha",
                   "Environment :: Console",
                   "Intended Audience :: End Users/Desktop",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: OS Independent",
                   "Topic :: Internet :: WWW/HTTP",
                   "Topic :: Database :: Front-Ends",
                   "Topic :: Communications :: Chat"],
      long_description=open("README.rst").read(),
      options={'test': {'verbose': False,
                        'coverage': False}})
