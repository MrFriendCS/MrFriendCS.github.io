CREATE TABLE port (
	port_code TEXT NOT NULL CHECK(LENGTH(port_code) = 3),
	port_name TEXT NOT NULL,
	local_authority TEXT NOT NULL,
	marine_region TEXT NOT NULL,
	service_type TEXT NOT NULL,
	PRIMARY KEY(port_code)
);
