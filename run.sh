#!/bin/sh
pdm makemigrations
pdm migrate
pdm collectstatic --no-input
pdm startdev 0.0.0.0:8000