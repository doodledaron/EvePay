import React from 'react'
import Image from 'next/image'

const Categories = () => {
  return (
    <div>
      <div className='pt-3 pb-6 flex flex-row items-center space-x-12'>
        <div className='pb-3 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-300 hover:opacity-100'>
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
            <path strokeLinecap="round" strokeLinejoin="round" d="M9.568 3H5.25A2.25 2.25 0 0 0 3 5.25v4.318c0 .597.237 1.17.659 1.591l9.581 9.581c.699.699 1.78.872 2.607.33a18.095 18.095 0 0 0 5.223-5.223c.542-.827.369-1.908-.33-2.607L11.16 3.66A2.25 2.25 0 0 0 9.568 3Z" />
            <path strokeLinecap="round" strokeLinejoin="round" d="M6 6h.008v.008H6V6Z" />
          </svg>
          <span className='text-xs'>icons</span>
        </div>

        <div className='pb-3 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-300 hover:opacity-100'>
          <Image
            src='/pool_icon.jpg'
            alt='Category - Pool'
            width={20}
            height={20}
          />
          <span className='text-xs'>Amazing Pools</span>
        </div>

        <div className='pb-3 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-300 hover:opacity-100'>
          <Image
            src='/views_icon.jpg'
            alt='Category - Views'
            width={20}
            height={20}
          />
          <span className='text-xs'>Amazing Views</span>
        </div>

        <div className='pb-3 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-300 hover:opacity-100'>
          <Image
            src='/beach_icon.jpg'
            alt='Category - Beachfront'
            width={20}
            height={20}
          />
          <span className='text-xs'>Beachfront</span>
        </div>

        <div className='pb-3 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-300 hover:opacity-100'>
          <Image
            src='/boats_icon.jpg'
            alt='Category - Boats'
            width={20}
            height={20}
          />
          <span className='text-xs'>Boats</span>
        </div>

        <div className='pb-3 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-300 hover:opacity-100'>
          <Image
            src='/omg_icon.jpg'
            alt='Category - OMG!'
            width={20}
            height={20}
          />
          <span className='text-xs'>OMG!</span>
        </div>

        <div className='pb-3 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-300 hover:opacity-100'>
          <Image
            src='/countryside_icon.jpg'
            alt='Category - Countryside'
            width={20}
            height={20}
          />
          <span className='text-xs'>Countryside</span>
        </div>

        <div className='pb-3 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-300 hover:opacity-100'>
          <Image
            src='/farms_icon.jpg'
            alt='Category - Farms'
            width={20}
            height={20}
          />
          <span className='text-xs'>Farms</span>
        </div>

        <div className='pb-3 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-300 hover:opacity-100'>
          <Image
            src='/tinyhome_icon.jpg'
            alt='Category - Tiny Homes'
            width={20}
            height={20}
          />
          <span className='text-xs'>Tiny Homes</span>
        </div>

        <div className='pb-3 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-300 hover:opacity-100'>
          <Image
            src='/mansion_icon.jpg'
            alt='Category - Mansions'
            width={20}
            height={20}
          />
          <span className='text-xs'>Mansions</span>
        </div>

        <div className='pb-3 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-300 hover:opacity-100'>
          <Image
            src='/cabins_icon.jpg'
            alt='Category - Cabins'
            width={20}
            height={20}
          />
          <span className='text-xs'>Cabins</span>
        </div>

        <div className='pb-3 flex flex-col items-center space-y-2 border-b-2 border-white opacity-60 hover:border-gray-300 hover:opacity-100'>
          <Image
            src='/room_icon.jpg'
            alt='Category - Rooms'
            width={20}
            height={20}
          />
          <span className='text-xs'>Rooms</span>
        </div>
        
      </div>
    </div>
  )
}

export default Categories
