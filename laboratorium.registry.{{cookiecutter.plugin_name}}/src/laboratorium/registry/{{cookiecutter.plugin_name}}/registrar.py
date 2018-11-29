# -*- coding: utf-8 -*-
"""
:mod:`laboratorium.facility.{{ cookiecutter.plugin_name }}.registrar -- TODO 
============================{{ '=' * cookiecutter.plugin_name|length }}========

.. module:: registrar 
    :platform: Unix
    :synopsis: TODO

TODO: Write long description

"""
from laboratorium.core.registrar import Registrar


class {{ cookiecutter.registrar_class_name }}(Registrar):
    """
    """

    def __init__(self):
        """
        """
        pass

    def register_studies(self, studies):
        """
        """
        raise NotImplemented()

    def register_experiments(self, experiments):
        """
        """
        raise NotImplemented()

    def register_trials(self, trials):
        """
        """
        raise NotImplemented()

    def register_variables(self, variables):
        """
        """
        raise NotImplemented()

    def register_measurements(self, measurements):
        """
        """
        raise NotImplemented()

    def reserve(self, executable):
        """
        """
        raise NotImplemented()

    def mark_completed(self, executable):
        """
        """
        raise NotImplemented()

    def retrieve(self, study=None, status=None):
        """
        """
        raise NotImplemented()

    def retrieve_experiments(self, study):
        """
        """
        raise NotImplemented()

    def retrieve_trials(self, experiment):
        """
        """
        raise NotImplemented()

    def retrieve_variables(self, trial):
        """
        """
        raise NotImplemented()

    def retrieve_measurements(self, variable):
        """
        """
        raise NotImplemented()
