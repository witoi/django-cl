# -*- coding: utf-8 -*-
"""
Unique Territorial Code
REGION-PROVINCIA-COMUNA

Description:
A list of Chilean regions, provinces and communes with
its codes as "choices" for form field. 

source:
http://www.subdere.gov.cl/sites/default/files/documentos/cod._terr._15_rgs..pdf
"""

REGION_CHOICES = (
    ('01', u'Región de Tarapacá'),
    ('02', u'Región de Antofagasta'),
    ('03', u'Región de Atacama'),
    ('04', u'Región de Coquimbo'),
    ('05', u'Región de Valparaíso'),
    ('06', u'Región del Libertador General Bernardo O\'Higgins'),
    ('07', u'Región del Maule'),
    ('08', u'Región del Biobío'),
    ('09', u'Región de La Araucanía'),
    ('10', u'Región de Los Lagos'),
    ('11', u'Región de Aisén del General Carlos Ibañez del Campo'),
    ('12', u'Región de Magallanes y de la Antártica Chilena'),
    ('13', u'Región Metropolitana de Santiago'),
    ('14', u'Región de Los Ríos'),    
    ('15', u'Región de Arica y Parinacota'),
)

PROVINCIA_CHOICES = (
    # ('15', u'Región de Arica y Parinacota'),
    ('151', u'Arica'),
    ('152', u'Parinacota'),

    # ('01', u'Región de Tarapacá'),
    ('011', u'Iquique'),
    ('014', u'Tamarugal'),

    # ('02', u'Región de Antofagasta'),
    ('021', u'Antofagasta'),
    ('022', u'El Loa'),
    ('023', u'Tocopilla'),

    # ('03', u'Región de Atacama'),
    ('031', u'Copiapó'),
    ('032', u'Chañaral'),
    ('033', u'Huasco'),

    # ('04', u'Región de Coquimbo'),
    ('041', u'Elqui'),
    ('042', u'Choapa'),
    ('043', u'Limarí'),

    # ('05', u'Región de Valparaíso'),
    ('051', u'Valparaíso'),
    ('052', u'Isla de Pascua'),
    ('053', u'Los Andes'),
    ('054', u'Petorca'),
    ('055', u'Quillota'),
    ('056', u'San Antonio'),
    ('057', u'San Felipe de Aconcagua'),
    ('058', u'Marga Marga'),

    # ('06', u'Región del Libertador General Bernardo O\'Higgins'),
    ('061', u'Cachapoal'),
    ('062', u'Cardenal Caro'),
    ('063', u'Colchagua'),

    # ('07', u'Región del Maule'),
    ('071', u'Talca'),
    ('072', u'Cauquenes'),
    ('073', u'Curicó'),
    ('074', u'Linares'),

    # ('08', u'Región del Biobío'),
    ('081', u'Concepción'),
    ('082', u'Arauco'),
    ('083', u'Biobío'),
    ('084', u'Ñuble'),

    # ('09', u'Región de La Araucanía'),
    ('091', u'Cautín'),
    ('092', u'Malleco'),

    # ('14', u'Región de Los Ríos'),    
    ('141', u'Valdivia'),
    ('142', u'Ranco'),

    # ('10', u'Región de Los Lagos'),
    ('101', u'Llanquihue'),
    ('102', u'Chiloé'),
    ('103', u'Osorno'),
    ('104', u'Palena'),

    # ('11', u'Región de Aisén del General Carlos Ibañez del Campo'),
    ('111', u'Coihaique'),
    ('112', u'Aisén'),
    ('113', u'Capitán Prat'),
    ('114', u'General Carrera'),

    # ('12', u'Región de Magallanes y de la Antártica Chilena'),
    ('121', u'Magallanes'),
    ('122', u'Antártica Chilena'),
    ('123', u'Tierra del Fuego'),
    ('124', u'Última Esperanza'),

    # ('13', u'Región Metropolitana de Santiago'),
    ('131', u'Santiago'),
    ('132', u'Cordillera'),
    ('133', u'Chacabuco'),
    ('134', u'Maipo'),
    ('135', u'Melipilla'),
    ('136', u'Talagante'),
)

COMUNA_CHOICES = (
    # ('15', u'Región de Arica y Parinacota'),
    # ('151', u'Arica'),
    ('15101', u'Arica'),
    ('15102', u'Camarones'),

    # ('152', u'Parinacota'),
    ('15201', u'Putre'),
    ('15202', u'General '),

    # ('01', u'Región de Tarapacá'),
    # ('011', u'Iquique'),
    ('01101', u'Iquique'),
    ('01107', u'Alto Hospicio'),
    # ('014', u'Tamarugal'),
    ('01401', u'Pozo Almonte'),
    ('01402', u'Camiña'),
    ('01403', u'Colchane'),
    ('01404', u'Huara'),
    ('01405', u'Pica'),

    # ('02', u'Región de Antofagasta'),
    # ('021', u'Antofagasta'),
    ('02101', u'Antofagasta'),
    ('02102', u'Mejillones'),
    ('02103', u'Sierra Gorda'),
    ('02104', u'Taltal'),

    # ('022', u'El Loa'),
    ('02201', u'Calama'),
    ('02202', u'Ollagüe'),
    ('02203', u'San Pedro de Atacama'),

    # ('023', u'Tocopilla'),
    ('02301', u'Tocopilla'),
    ('02302', u'María Elena'),

    # ('03', u'Región de Atacama'),
    # ('031', u'Copiapó'),
    ('03101', u'Copiapó'),
    ('03102', u'Caldera'),
    ('03103', u'Tierra Amarilla'),

    # ('032', u'Chañaral'),
    ('03201', u'Chañaral'),
    ('03202', u'Diego de Almagro'),

    # ('033', u'Huasco'),
    ('03301', u'Vallenar'),
    ('03302', u'Alto del Carmen'),
    ('03303', u'Freirina'),
    ('03304', u'Huasco'),


    # ('04', u'Región de Coquimbo'),
    # ('041', u'Elqui'),
    ('04101', u'La Serena'),
    ('04102', u'Coquimbo'),
    ('04103', u'Andacollo'),
    ('04104', u'La Higuera'),
    ('04105', u'Paiguano'),
    ('04106', u'Vicuña'),

    # ('042', u'Choapa'),
    ('04201', u'Illapel'),
    ('04202', u'Canela'),
    ('04203', u'Los Vilos'),
    ('04204', u'Salamanca'),

    # ('043', u'Limarí'),
    ('04301', u'Ovalle'),
    ('04302', u'Combarbalá'),
    ('04303', u'Monte Patria'),
    ('04304', u'Punitaqui'),
    ('04305', u'Río Hurtado'),

    # ('05', u'Región de Valparaíso'),
    # ('051', u'Valparaíso'),
    ('05101', u'Valparaíso'),
    ('05102', u'Casablanca'),
    ('05103', u'Concón'),
    ('05104', u'Juan Fernández'),
    ('05105', u'Puchuncaví'),
    ('05107', u'Quintero'),
    ('05109', u'Viña del Mar'),

    # ('052', u'Isla de Pascua'),
    ('05201', u'Isla de Pascua'),

    # ('053', u'Los Andes'),
    ('05301', u'Los Andes'),
    ('05302', u'Calle Larga'),
    ('05303', u'Rinconada'),
    ('05304', u'San Esteban'),

    # ('054', u'Petorca'),
    ('05401', u'La Ligua'),
    ('05402', u'Cabildo'),
    ('05403', u'Papudo'),
    ('05404', u'Petorca'),
    ('05405', u'Zapallar'),

    # ('055', u'Quillota'),
    ('05501', u'Quillota'),
    ('05502', u'Calera'),
    ('05503', u'Hijuelas'),
    ('05504', u'La Cruz'),
    ('05506', u'Nogales'),

    # ('056', u'San Antonio'),
    ('05601', u'San Antonio'),
    ('05602', u'Algarrobo'),
    ('05603', u'Cartagena'),
    ('05604', u'El Quisco'),
    ('05605', u'El Tabo'),
    ('05606', u'Santo Domingo'),

    # ('057', u'San Felipe de Aconcagua'),
    ('05701', u'San Felipe'),
    ('05702', u'Catemu'),
    ('05703', u'Llaillay'),
    ('05704', u'Panquehue'),
    ('05705', u'Putaendo'),
    ('05706', u'Santa María'),

    # ('058', u'Marga Marga'),
    ('05801', u'Quilpué'),
    ('05801', u'Limache'),
    ('05801', u'Olmué'),
    ('05801', u'Villa Alemana'),


    # ('06', u'Región del Libertador General Bernardo O\'Higgins'),
    # ('061', u'Cachapoal'),
    ('06101', u'Rancagua'),
    ('06102', u'Codegua'),
    ('06103', u'Coinco'),
    ('06104', u'Coltauco'),
    ('06105', u'Doñihue'),
    ('06106', u'Graneros'),
    ('06107', u'Las Cabras'),
    ('06108', u'Machalí'),
    ('06109', u'Malloa'),
    ('06110', u'Mostazal'),
    ('06111', u'Olivar'),
    ('06112', u'Peumo'),
    ('06113', u'Pichidegua'),
    ('06114', u'Quinta de Tilcoco'),
    ('06115', u'Rengo'),
    ('06116', u'Requínoa'),
    ('06117', u'San Vicente'),

    # ('062', u'Cardenal Caro'),
    ('06201', u'Pichilemu'),
    ('06202', u'La Estrella'),
    ('06203', u'Litueche'),
    ('06204', u'Marchihue'),
    ('06205', u'Navidad'),
    ('06206', u'Paredones'),

    # ('063', u'Colchagua'),
    ('06301', u'San Fernando'),
    ('06302', u'Chépica'),
    ('06303', u'Chimbarongo'),
    ('06304', u'Lolol'),
    ('06305', u'Nancagua'),
    ('06306', u'Palmilla'),
    ('06307', u'Peralillo'),
    ('06308', u'Placilla'),
    ('06309', u'Pumanque'),
    ('06310', u'Santa Cruz'),


    # ('07', u'Región del Maule'),
    # ('071', u'Talca'),
    ('07101', u'Talca'),
    ('07102', u'Constitución'),
    ('07103', u'Curepto'),
    ('07104', u'Empedrado'),
    ('07105', u'Maule'),
    ('07106', u'Pelarco'),
    ('07107', u'Pencahue'),
    ('07108', u'Río Claro'),
    ('07109', u'San Clemente'),
    ('07110', u'San Rafael'),
    ('07201', u'Cauquenes'),

    # ('072', u'Cauquenes'),
    ('07202', u'Chanco'),
    ('07203', u'Pelluhue'),

    # ('073', u'Curicó'),
    ('07301', u'Curicó'),
    ('07302', u'Hualañe'),
    ('07303', u'Licantén'),
    ('07304', u'Molina'),
    ('07305', u'Rauco'),
    ('07306', u'Romeral'),
    ('07307', u'Sagrada Familia'),
    ('07308', u'Teno'),
    ('07309', u'Vichuquén'),
    # ('074', u'Linares'),
    ('07401', u'Linares'),
    ('07402', u'Colbún'),
    ('07403', u'Longaví'),
    ('07404', u'Parral'),
    ('07405', u'Retiro'),
    ('07406', u'San Javier'),
    ('07407', u'Villa Alegre'),
    ('07408', u'Yerbas Buenas'),


    # ('08', u'Región del Biobío'),
    # ('081', u'Concepción'),
    ('08101', u'Concepción'),
    ('08102', u'Coronel'),
    ('08103', u'Chiguayante'),
    ('08104', u'Florida'),
    ('08105', u'Hualqui'),
    ('08106', u'Lota'),
    ('08107', u'Penco'),
    ('08108', u'San Pedro de la Paz'),
    ('08109', u'Santa Juana'),
    ('08110', u'Talcahuano'),
    ('08111', u'Tompe'),
    ('08112', u'Hualpén'),

    # ('082', u'Arauco'),
    ('08201', u'Lebu'),
    ('08202', u'Arauco'),
    ('08203', u'Cañeete'),
    ('08204', u'Contulmo'),
    ('08205', u'Curanilahue'),
    ('08206', u'Los Alamos'),
    ('08207', u'Tirúa'),

    # ('083', u'Biobío'),
    ('08301', u'Los Angeles'),
    ('08302', u'Antuco'),
    ('08303', u'Cabrero'),
    ('08304', u'Laja'),
    ('08305', u'Mulchén'),
    ('08306', u'Nacimiento'),
    ('08307', u'Negrete'),
    ('08308', u'Quilaco'),
    ('08309', u'Quilleco'),
    ('08310', u'San Rosendo'),
    ('08311', u'Santa Bárbara'),
    ('08312', u'Tucapel'),
    ('08313', u'Yumbel'),
    ('08314', u'Alto Biobío'),

    # ('084', u'Ñuble'),
    ('08401', u'Chillán'),
    ('08402', u'Bulnes'),
    ('08403', u'Cobquecura'),
    ('08404', u'Coelemu'),
    ('08405', u'Coihueco'),
    ('08406', u'Chillán Viejo'),
    ('08407', u'El Carmen'),
    ('08408', u'Ninhue'),
    ('08409', u'Ñiquén'),
    ('08410', u'Pemuco'),
    ('08411', u'Pinto'),
    ('08412', u'Portezuelo'),
    ('08413', u'Quillón'),
    ('08414', u'Quirihue'),
    ('08415', u'Ráuil'),
    ('08416', u'San Carlos'),
    ('08417', u'San Fabián'),
    ('08418', u'San Ignacio'),
    ('08419', u'San Nicolás'),
    ('08420', u'Treguaco'),
    ('08421', u'Yungay'),


    # ('09', u'Región de La Araucanía'),
    # ('091', u'Cautín'),
    ('09101', u'Temuco'),
    ('09102', u'Carahue'),
    ('09103', u'Cunco'),
    ('09104', u'Curarrehue'),
    ('09105', u'Freire'),
    ('09106', u'Galvarino'),
    ('09107', u'Gorbea'),
    ('09108', u'Lautaro'),
    ('09109', u'Loncoche'),
    ('09110', u'Melipeuco'),
    ('09111', u'Nueva Imperial'),
    ('09112', u'Padre Las Casas'),
    ('09113', u'Perquenco'),
    ('09114', u'Pitrufquén'),
    ('09115', u'Pucón'),
    ('09116', u'Saavedra'),
    ('09117', u'Teodoro Schmidt'),
    ('09118', u'Toltén'),
    ('09119', u'Vilcún'),
    ('09120', u'Villarrica'),
    ('09121', u'Cholchol'),

    # ('092', u'Malleco'),
    ('09201', u'Angol'),
    ('09202', u'Collipulli'),
    ('09203', u'Curacautín'),
    ('09204', u'Ercilla'),
    ('09205', u'Lonquimay'),
    ('09206', u'Los Sauces'),
    ('09207', u'Lumaco'),
    ('09208', u'Purén'),
    ('09209', u'Renaico'),
    ('09210', u'Traiguén'),
    ('09211', u'Victoria'),


    # ('14', u'Región de Los Ríos'),    
    # ('141', u'Valdivia'),
    ('14101', u'Valdivia'),
    ('14102', u'Corral'),
    ('14103', u'Lanco'),
    ('14104', u'Los Lagos'),
    ('14105', u'Máfil'),
    ('14106', u'Mariquina'),
    ('14107', u'Paillaco'),
    ('14108', u'Panguipulli'),
    # ('142', u'Ranco'),
    ('14201', u'La Unión'),
    ('14202', u'Futrono'),
    ('14203', u'Lago Ranco'),
    ('14204', u'Río Bueno'),



    # ('10', u'Región de Los Lagos'),
    # ('101', u'Llanquihue'),
    ('10101', u'Puerto Montt'),
    ('10102', u'Calbuco'),
    ('10103', u'Cochamó'),
    ('10104', u'Fresia'),
    ('10105', u'Frutillar'),
    ('10106', u'Los Muermos'),
    ('10107', u'Llanquihue'),
    ('10108', u'Maullín'),
    ('10109', u'Puerto Varas'),

    # ('102', u'Chiloé'),
    ('10201', u'Castro'),
    ('10202', u'Ancud'),
    ('10203', u'Chonchi'),
    ('10204', u'Curaco de Vélez'),
    ('10205', u'Dalcahue'),
    ('10206', u'Puqueldón'),
    ('10207', u'Queilén'),
    ('10208', u'Quellón'),
    ('10209', u'Quemchi'),
    ('10210', u'Quinchao'),

    # ('103', u'Osorno'),
    ('10301', u'Osorno'),
    ('10302', u'Puerto Octay'),
    ('10303', u'Purranque'),
    ('10304', u'Puyehue'),
    ('10305', u'Río Negro'),
    ('10306', u'San Juan de la Costa'),
    ('10307', u'San Pablo'),

    # ('104', u'Palena'),
    ('10401', u'Chaitén'),
    ('10402', u'Futaleufú'),
    ('10403', u'Hualaihué'),
    ('10404', u'Palena'),


    # ('11', u'Región de Aisén del General Carlos Ibañez del Campo'),
    # ('111', u'Coihaique'),
    ('11101', u'Coihaique'),
    ('11102', u'Lago Verde'),

    # ('112', u'Aisén'),
    ('11201', u'Aisén'),
    ('11202', u'Cisnes'),
    ('11203', u'Guaitecas'),

    # ('113', u'Capitán Prat'),
    ('11301', u'Cochrane'),
    ('11302', u'O\'Higgins'),
    ('11303', u'Tortel'),

    # ('114', u'General Carrera'),
    ('11401', u'Chile Chico'),
    ('11402', u'Río Ibáñez'),


    # ('12', u'Región de Magallanes y de la Antártica Chilena'),
    # ('121', u'Magallanes'),
    ('12101', u'Punta Arenas'),
    ('12102', u'Laguna Blanca'),
    ('12103', u'Río Verde'),
    ('12104', u'San Gregorio'),

    # ('122', u'Antártica Chilena'),
    ('12201', u'Cabo de Hornos'),
    ('12202', u'Antártica'),

    # ('123', u'Tierra del Fuego'),
    ('12301', u'Porvenir'),
    ('12302', u'Primavera'),
    ('12303', u'Timaukel'),

    # ('124', u'Última Esperanza'),
    ('12401', u'Natales'),
    ('12402', u'Torres del Paine'),


    # ('13', u'Región Metropolitana de Santiago'),
    # ('131', u'Santiago'),
    ('13101', u'Santiago'),
    ('13102', u'Cerrillos'),
    ('13103', u'Cerro Navia'),
    ('13104', u'Conchalí'),
    ('13105', u'El Bosque'),
    ('13106', u'Estación Central'),
    ('13107', u'Huechuraba'),
    ('13108', u'Independencia'),
    ('13109', u'La Cisterna'),
    ('13110', u'La Florida'),
    ('13111', u'La Granja'),
    ('13112', u'La Pintana'),
    ('13113', u'La Reina'),
    ('13114', u'Las Condes'),
    ('13115', u'Lo Barnechea'),
    ('13116', u'Lo Espejo'),
    ('13117', u'Lo Prado'),
    ('13118', u'Macul'),
    ('13119', u'Maipú'),
    ('13120', u'Ñuñoa'),
    ('13121', u'Pedro Aguirre Cerda'),
    ('13122', u'Peñalolén'),
    ('13123', u'Providencia'),
    ('13124', u'Pudahuel'),
    ('13125', u'Quilicura'),
    ('13126', u'Quinta Normal'),
    ('13127', u'Recoleta'),
    ('13128', u'Renca'),
    ('13129', u'San Joaquín'),
    ('13130', u'San Miguel'),
    ('13131', u'San Ramón'),
    ('13132', u'Vitacura'),

    # ('132', u'Cordillera'),
    ('13201', u'Puente Alto'),
    ('13202', u'Pirque'),
    ('13203', u'San José de Maipo'),

    # ('133', u'Chacabuco'),
    ('13301', u'Colina'),
    ('13302', u'Lampa'),
    ('13303', u'Tiltil'),

    # ('134', u'Maipo'),
    ('13401', u'San Bernardo'),
    ('13402', u'Buin'),
    ('13403', u'Calera de Tango'),
    ('13404', u'Paine'),

    # ('135', u'Melipilla'),
    ('13501', u'Melipilla'),
    ('13502', u'Alhué'),
    ('13503', u'Curacaví'),
    ('13504', u'María Pinto'),
    ('13505', u'San Pedro'),

    # ('136', u'Talagante'),
    ('13601', u'Talagante'),
    ('13602', u'El Monte'),
    ('13603', u'Isla de Maipo'),
    ('13604', u'Padre Hurtado'),
    ('13605', u'Peñaflor'),
)

# Makes a choice of provinces grouped by region, keeping regions
# sorted by code

regiones_names = [r[1] for r in sorted(REGION_CHOICES, key=lambda x: x[0])]
_rpc_dict = dict([(name,[]) for name in regiones_names])

# Puts provices in regions
for r in REGION_CHOICES:
    for p in PROVINCIA_CHOICES:
        if p[0][:2] == r[0]:
            _rpc_dict[r[1]].append(p)

# Makes a sorted list
_rpc_list = []
for name in regiones_names:
    _rpc_list.append((name, tuple(_rpc_dict[name])))
    
# Makes a tuple
REGION_PROVINCIA_CHOICES = tuple(_rpc_list)

# Makes a choice of communes grouped by provice, keeping communes
# sorted by code
provices_name = [r[1] for r in sorted(PROVINCIA_CHOICES, key=lambda x: x[0])]
_pcc_dict = dict([(name,[]) for name in provices_name])

# puts provices in regions
for p in PROVINCIA_CHOICES:
    for c in COMUNA_CHOICES:
        if c[0][:3] == p[0]:
            _pcc_dict[p[1]].append(c)

# makes a sorted list
_pcc_list = []
for name in provices_name:
    _pcc_list.append((name, tuple(_pcc_dict[name])))
    
# makes a tuple
PROVINCIA_COMUNA_CHOICES = tuple(_pcc_list)
