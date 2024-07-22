import React from 'react'
import Image from 'next/image'
import Link from 'next/link'

const PropertyListItem = ({ id, name }: { id: number; name: string }) => {
  return (
    <div>
      <div key={id} className="cursor-pointer">
        <div className="relative overflow-hidden aspect-square rounded-xl">
          <Image
            fill
            src='/beach_1.jpg'
            sizes="(max-width: 768px) 768px, (max-width: 1200px): 768px, 768px"
            className="hover:scale-110 object-cover transition h-full w-full"
            alt="Beach house"
          />
        </div>

        <div className="mt-2">
          <p className="text-lg font-bold">property name</p>
        </div>

        <div className="mt-2">
          <p className="text-sm text-gray-500"><strong>$200</strong></p>
        </div>


        <Link href={`/properties/${id}`}>
          <p>View Property</p>
        </Link>
      </div>
    </div>
  )
}

export default PropertyListItem
