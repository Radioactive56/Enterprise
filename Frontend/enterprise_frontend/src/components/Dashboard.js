import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGrid, GridToolbar } from '@mui/x-data-grid';
import { useMovieData } from '@mui/x-data-grid-generator';

const VISIBLE_FIELDS = ['title', 'company', 'director', 'year', 'cinematicUniverse'];

export default function Dashboard() {
    const data = useMovieData();

    // Otherwise filter will be applied on fields such as the hidden column id
    const columns = React.useMemo(
      () => data.columns.filter((column) => VISIBLE_FIELDS.includes(column.field)),
      [data.columns],
    );
  return (
    <div>
       <Box sx={{ height: 400, width: 1 }}>
      <DataGrid
        {...data}
        disableColumnFilter
        disableColumnSelector
        disableDensitySelector
        columns={columns}
        slots={{ toolbar: GridToolbar }}
        slotProps={{
          toolbar: {
            showQuickFilter: true,
          },
        }}
      />
    </Box>
    </div>
  )
}
