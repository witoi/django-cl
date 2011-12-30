=======================
 Django CL Localflavor
=======================

About
-----

Based on https://code.djangoproject.com/ticket/11762

The idea of this package is contain all cl localflavor improvements
that are not in Django, to improve them to be part of Django actually.


What is on Django
-----------------

The content of django.contrin.localflavor.cl is

- forms.py

  + CLRegionSelect
  + CLRutField

- cl_regions.py

  + REGION_CHOICES


This package adds
-----------------

Regiones, comunas and provicias
...............................

The idea is to get 'regiones', 'provicias' and 'comunas' in a way
they can be used in forms as field's choices.

- forms.py

  + class CLProvinciaSelect
  + class CLComunaSelect

- cl_reg_prov_com.py

  + REGION_CHOICES
  + PROVINCIA_CHOICES
  + COMUNA_CHOICES
  + REGION_PROVICIA_CHOICES
  + PROVINCIA_COMUNA_CHOICES
