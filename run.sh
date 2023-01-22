#!/bin/sh
pdm makemigrations
pdm migrate
pdm collectstatic --no-input
pdm fetchcompany
pdm startdev
