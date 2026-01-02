// Helper functions
export const formatDate = (date) => {
  return new Date(date).toLocaleDateString();
};

export const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));
