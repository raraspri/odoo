
# -*- encoding: utf-8 -*-
##############################################################################
#
#    Universidad Pablo de Olavide - Sevilla
#
#    
#
#    
#    
#    Módulo diseñado para la Gestión de una revista
#
##############################################################################
{
    "name": "moleqla",
    "version": "1.0",
    "depends": ["base"],
    "author": "R. Rastrero",
    "category": "Moleqla",
    "description": """
       ERP Revista
    """,
    "init_xml": [],
                  
    'update_xml': [
                        'Views/articulo_graph_view.xml',
                        'Views/autor_view.xml',
                        'Views/seccion_view.xml',
                        'Views/maquetador_view.xml',
                        'Views/editor_view.xml',
                        'Views/articulo_view.xml',
                        'Views/revision_view.xml',
                        'Views/maquetacion_view.xml',
                        'Views/numero_view.xml',
                        'Views/correo_view.xml',
                        'Views/destaque_articulos_view.xml',
                        'Views/votacion_view.xml',
                        'Views/linea_votacion_view.xml',
                        'Workflows/articulo_workflow.xml',
                        
						
                       ],
    'demo_xml': [],
    'installable': True,
    #'application': True,
    'images': [], #iconos
#    'certificate': 'certificate',
}