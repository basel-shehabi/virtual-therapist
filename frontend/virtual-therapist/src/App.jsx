import { Card, CardActions, CardContent, Typography, TextField, Button } from '@mui/material'
import SendIcon from '@mui/icons-material/Send';

function App() {
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '50vh' }}>
      <Card style={{ margin: 'auto' }}>
        <CardContent>
          <Typography>
            Welcome to Virtual Therapy! Your AI Powered Assistant!
          </Typography>
          <br/>
          <Typography variant="body2" color="text.secondary" align="center">
            What's on your mind today?
          </Typography>
          <br/>
          <CardActions style={{ justifyContent: 'center'}}> 
            <TextField variant="outlined" id="outlined-basic"/>
            <Button endIcon={<SendIcon />}></Button>
          </CardActions>
        </CardContent>
      </Card>
    </div>
  )
}

export default App
