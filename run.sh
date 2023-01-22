#!/bin/sh
pdm makemigrations
pdm migrate
pdm collectstatic --no-input
pdm createdefaultuser
pdm fetchcompanies
pdm fetchproducts
pdm fetchcompanyproducts
pdm startdev
