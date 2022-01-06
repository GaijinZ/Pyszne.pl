let autocomplete;
let addressField;
let apartmentNumber;
let postalField;

function initAutocomplete() {
  addressField = document.querySelector("#ship-address");
  apartmentNumber = document.querySelector("#apartment-number");
  postalField = document.querySelector("#postcode");
  autocomplete = new google.maps.places.Autocomplete(addressField, {
    componentRestrictions: { country: 'pl' },
    fields: ["address_components", "geometry"],
    types: ["address"],
  });
  addressField.focus();
  autocomplete.addListener("place_changed", fillInAddress);
}

function fillInAddress() {

  const place = autocomplete.getPlace();
  let buildingNumber = "";
  let streetName = "";
  let postcode = "";
  let city = '';

  for (const component of place.address_components) {
    const componentType = component.types[0];

    switch (componentType) {

      case "street_number": {
        buildingNumber = component.long_name;
        break;
      }

      case "route": {
        streetName = component.short_name;
        break;
      }

      case "postal_code": {
        postcode = component.long_name;
        break;
      }

      case "postal_code_suffix": {
        postcode = `${postcode}-${component.long_name}`;
        break;
      }
      case "locality":
        city = component.long_name
        break;
    }
  }

  addressField.value = streetName + ' ' + buildingNumber + ', ' + postcode + ' ' + city;
}
