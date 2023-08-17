steps = [
    [
       ## Create the table
        """
        CREATE TABLE appointments (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(1000) NOT NULL,
            date TIMESTAMP(0) WITH TIME ZONE,
            description TEXT NOT NULL,
            price SMALLINT NOT NULL
        );
        """,
       ## Drop the table
       """
       DROP TABLE appointments;
       """
    ]
]
