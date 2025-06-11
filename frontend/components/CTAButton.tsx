import { motion } from 'framer-motion';
import React from 'react';

export function CTAButton({ children }: { children: React.ReactNode }) {
  return (
    <motion.button
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 0.95 }}
      className="px-4 py-2 bg-primary text-primary-foreground rounded"
    >
      {children}
    </motion.button>
  );
}
