#!/bin/sh
pdm makemigrations
pdm migrate
pdm collectstatic
pdm startdev