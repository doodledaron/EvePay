'use client';

import React, { useEffect, ReactNode } from 'react';
import AOS from 'aos';
import 'aos/dist/aos.css';

interface AosWrapperProps {
  children: ReactNode;
  animationType: string;
  duration?: number;
  easing?: string;
  delay?: number;
}

const AosWrapper: React.FC<AosWrapperProps> = ({
  children,
  animationType,
  duration = 1200,
  easing = 'ease-in-out',
  delay = 0, 
}) => {
  useEffect(() => {
    AOS.init({
      duration,
      easing,
      once: true,
    });
  }, [duration, easing]);

  return (
    <div data-aos={animationType} data-aos-delay={delay}>
      {children}
    </div>
  );
};

export default AosWrapper;
