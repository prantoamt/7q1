#!/bin/sh
pdm makemigrations
pdm migrate
pdm collectstatic --no-input
pdm fetchcompanies
pdm fetchproducts
pdm fetchcompanyproducts
pdm startdev
