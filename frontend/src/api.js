import axios from "axios";

const BASE_URL = "http://localhost:5000";

export const getSegments = async () => {
  const response = await axios.get(`${BASE_URL}/segments`);
  return response.data;
};

export const getCustomers = async () => {
  const response = await axios.get(`${BASE_URL}/customers`);
  return response.data;
};

export const getChampions = async () => {
  const response = await axios.get(`${BASE_URL}/champions`);
  return response.data;
};