-- SELECT t.ticket_id, u.name AS passenger, r.origin, r.destination, p.name AS plane_name, r.departure_time,   r.arrival_time
--     FROM ticket t
--     JOIN users u ON t.user_id = u.id
--     JOIN routes r ON t.route_id = r.route_id
--     JOIN plane p ON t.plane_id = p.plane_id
--     WHERE t.user_id = 2;


-- SELECT gender
-- FROM ticket
-- WHERE  seat_number = 12 and route_id = 'R002';


SELECT * FROM routes
WHERE departure_time > now();