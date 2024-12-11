'''Input/Label info used for generating New Hike form markup
'''
new_hike_form_content = {
    'hike_date': {
        'name': 'hike_date',
        'label': 'Hike date',
        'inputType': 'date',
        'required': True
    },
    'area_name': {
        'name': 'area_name',
        'label': 'Area',
        'inputType': 'text',
        'required': True
    },
    'trailhead': {
        'name': 'trailhead',
        'label': 'Trailhead',
        'inputType': 'text',
        'required': True

    },
    'trails_cs': {
        'name': 'trails_cs',
        'label': 'Trails (comma-separated)',
        'inputType': 'text',
        'required': True
    },
    'distance_km': {
        'name': 'distance_km',
        'label': 'Distance (KM)',
        'inputType': 'number',
        'required': True
    },
    'image_url': {
        'name': 'image_url',
        'label': 'Image URL',
        'inputType': 'text',
        'required': False
    },
    'image_alt': {
        'name': 'image_alt',
        'label': 'Image description',
        'inputType': 'text',
        'required': False
    },
    'map_link': {
        'name': 'map_link',
        'label': 'Map link',
        'inputType': 'text',
        'required': False
    },
    'other_info': {
        'name': 'other_info',
        'label': 'Description',
        'inputType': 'text',
        'required': False
    }
}
