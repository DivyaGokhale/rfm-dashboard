const BASE_URL = "http://localhost:5000";

export const getSegments = async () => {
  const res = await fetch(`${BASE_URL}/segments`);
  return res.json();
};

export const getChampions = async () => {
  const res = await fetch(`${BASE_URL}/champions`);
  return res.json();
};
