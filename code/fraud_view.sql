create view fraudes as
with
window_funcs as (
	SELECT
		*
		, LAG(Cliente_Id) OVER (ORDER BY Cliente_Id, DataHora) pCLiente_Id
	    , LAG(DataHora) OVER (ORDER BY Cliente_Id, DataHora) pDataDate
	FROM Transacao t
),
filter_step as (
	select
		*
		, DATEDIFF(second, pDataDate, DataHora) as diff_in_seconds
	from window_funcs
	where
		pDataDate is not null
		and Cliente_Id = pCliente_Id
)
select *
from filter_step
where diff_in_seconds < 120