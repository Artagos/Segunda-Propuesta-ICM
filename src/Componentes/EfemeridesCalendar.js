import * as React from 'react';
import dayjs from 'dayjs';
import { DemoContainer, DemoItem } from '@mui/x-date-pickers/internals/demo';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DateCalendar } from '@mui/x-date-pickers/DateCalendar'; // Ajusta la ruta según tu estructura de archivos y asegúrate de haber importado el componente
import Badge from '@mui/material/Badge';
import { PickersDay } from '@mui/x-date-pickers/PickersDay';
import '../ComponentsCss/Efemeride.css'; // Ajusta la ruta según tu estructura de archivos y asegúrate de haber importado los estilos
function ServerDay(props) {
  const { highlightedDays = [], day, outsideCurrentMonth, ...other } = props;

  const isSelected =
    !props.outsideCurrentMonth && highlightedDays.indexOf(props.day.date()) >= 0;

  return (
    <Badge
      key={props.day.toString()}
      overlap="circular"
      badgeContent={isSelected ? '🌚' : undefined}
    >
      <PickersDay {...other} outsideCurrentMonth={outsideCurrentMonth} day={day} />
    </Badge>
  );
}


export default function DateCalendarFormProps() {
  const [highlightedDays, setHighlightedDays] = React.useState([1, 2, 15]);
  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <DemoContainer components={['DateCalendar']}>
      <DateCalendar
    defaultValue={dayjs('2022-04-17')}
    views={['month', 'day']}
    openTo="month"
    slots={{day: ServerDay}}
    slotProps={{
      day: {
        highlightedDays,
      },
    }}
  />

      </DemoContainer>
    </LocalizationProvider>
  );
}