import React, { useState, useEffect } from "react";
import { FlatList, Dimensions } from "react-native";

import { Container, Place, Title } from "./styles";

const Main = () => {
  const [places, setPlaces] = useState([]);

  useEffect(() => {
    async function loadPlaces() {
      const response = await fetch("http://localhost:3000/places");
      const data = await response.json();
      setPlaces(data);
    }
    loadPlaces();
  }, []);

  return (
    <Container>
      <FlatList
        contentContainerStyle={{ flexGrow: 1, justifyContent: "center" }}
        data={places}
        keyExtractor={place => String(place.id)}
        renderItem={({ item }) => (
          <Place width={Dimensions.get("window").width}>
            <Title>{item.name}</Title>
          </Place>
        )}
      />
    </Container>
  );
};

export default Main;
