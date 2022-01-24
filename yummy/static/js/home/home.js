let autocomplete;
let addressField;
let apartmentNumber;
let postalField;

function initAutocomplete() {
  addressField = document.querySelector('#ship-address');
  postalField = document.querySelector('#postcode');
  autocomplete = new google.maps.places.Autocomplete(addressField, {
    componentRestrictions: { country: 'pl' },
    fields: ['address_components', 'geometry'],
    types: ['address'],
  });
  addressField.focus();
  autocomplete.addListener('place_changed', fillInAddress);
}

function fillInAddress() {

  const place = autocomplete.getPlace();
  let fullAddress = '';

  for (const component of place.address_components) {
    const componentType = component.types[0];

    switch (componentType) {

      case 'route': {
        fullAddress += `${component.short_name}, `;
        break;
      }

      case 'street_number': {
        fullAddress += `${component.long_name} `;
        break;
      }

      case 'postal_code': {
        fullAddress += `${component.long_name} `;
        break;
      }

      case 'locality':
        fullAddress +=`${component.long_name} `
        break;
    }
  }
  postalField.value = fullAddress.split(' ')[3];
  addressField.value = fullAddress;
}
