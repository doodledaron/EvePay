// components/PropertyList.tsx
import React from 'react';
import PropertyListItem from './PropertyListItem';

const properties = [
  { id: 1, name: 'Property One' },
  { id: 2, name: 'Property Two' },
  // Add more properties as needed
];

const PropertyList = () => {
  return (
    <>
      {properties.map((property) => (
        <PropertyListItem key={property.id} id={property.id} name={property.name} />
      ))}
    </>
  );
}

export default PropertyList;