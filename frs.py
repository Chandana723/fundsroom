import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  // State variables
  const [preferences, setPreferences] = useState({
    dietary: [],
    tastes: [],
  });
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);

  // Fetch recommendations when preferences change
  useEffect(() => {
    if (preferences.dietary.length > 0 || preferences.tastes.length > 0) {
      setLoading(true);
      // Simulated API call - replace with actual backend endpoint
      axios.post('/api/recommendations', preferences)
        .then(response => {
          setRecommendations(response.data);
          setLoading(false);
        })
        .catch(error => {
          console.error('Error fetching recommendations:', error);
          setLoading(false);
        });
    }
  }, [preferences]);

  // Handle checkbox change for dietary preferences
  const handleDietaryChange = (e) => {
    const { value, checked } = e.target;
    setPreferences(prevPreferences => ({
      ...prevPreferences,
      dietary: checked ? [...prevPreferences.dietary, value] : prevPreferences.dietary.filter(pref => pref !== value)
    }));
  };

  // Handle checkbox change for taste preferences
  const handleTasteChange = (e) => {
    const { value, checked } = e.target;
    setPreferences(prevPreferences => ({
      ...prevPreferences,
      tastes: checked ? [...prevPreferences.tastes, value] : prevPreferences.tastes.filter(pref => pref !== value)
    }));
  };

  return (
    <div>
      <h1>Personalized Food Recommendations</h1>
      {/* Dietary preferences */}
      <div>
        <h2>Dietary Preferences</h2>
        <label>
          <input type="checkbox" value="vegan" onChange={handleDietaryChange} />
          Vegan
        </label>
        <label>
          <input type="checkbox" value="gluten-free" onChange={handleDietaryChange} />
          Gluten-Free
        </label>
        {/* Add more dietary preferences checkboxes as needed */}
      </div>
      {/* Taste preferences */}
      <div>
        <h2>Taste Preferences</h2>
        <label>
          <input type="checkbox" value="spicy" onChange={handleTasteChange} />
          Spicy
        </label>
        <label>
          <input type="checkbox" value="sweet" onChange={handleTasteChange} />
          Sweet
        </label>
        {/* Add more taste preferences checkboxes as needed */}
      </div>
      {/* Loading indicator */}
      {loading && <p>Loading recommendations...</p>}
      {/* Display recommendations */}
      <div>
        <h2>Recommendations</h2>
        <ul>
          {recommendations.map((recommendation, index) => (
            <li key={index}>
              <img src={recommendation.image} alt={recommendation.title} />
              <h3>{recommendation.title}</h3>
              <p>{recommendation.description}</p>
              {/* Add more recommendation details as needed */}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default App;
