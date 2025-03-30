import React, { useState } from "react";
import axios from "axios";

const Signup = () => {
  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    phone_number: "",
    password: "",
    role: "Customer",
  });

  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    if (!formData.full_name || !formData.email || !formData.phone_number || !formData.password) {
      setMessage("All fields are required!");
      setLoading(false);
      return;
    }

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/register/", formData);
      setMessage(response.data.message);
      setFormData({ full_name: "", email: "", phone_number: "", password: "", role: "Customer" });
    } catch (error) {
      setMessage(error.response?.data?.message || "Registration failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="bg-white p-6 rounded-lg shadow-md w-96">
        <h2 className="text-2xl font-semibold mb-4 text-center">Register</h2>
        {message && <p className="text-center text-red-500">{message}</p>}
        <form onSubmit={handleSubmit} className="space-y-3">
          <input
            type="text"
            name="full_name"
            value={formData.full_name}
            onChange={handleChange}
            placeholder="Full Name"
            className="w-full p-2 border rounded"
          />
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="Email"
            className="w-full p-2 border rounded"
          />
          <input
            type="text"
            name="phone_number"
            value={formData.phone_number}
            onChange={handleChange}
            placeholder="Phone Number"
            className="w-full p-2 border rounded"
          />
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            placeholder="Password"
            className="w-full p-2 border rounded"
          />
          <select name="role" value={formData.role} onChange={handleChange} className="w-full p-2 border rounded">
            <option value="Customer">Customer</option>
            <option value="Farmer">Farmer</option>
            <option value="Admin">Admin</option>
            <option value="Verifier">Verifier</option>
            <option value="HerbalExpert">Herbal Expert</option>
          </select>
          <button type="submit" className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700" disabled={loading}>
            {loading ? "Registering..." : "Register"}
          </button>
        </form>
      </div>
    </div>
  );
};

export default Signup;
