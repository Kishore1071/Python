import express, { json } from 'express'
import jwt from 'jsonwebtoken'
import { config } from 'dotenv'
import crypto from 'crypto'
import cors from 'cors'

const app = express()
config()
app.use(json()) 

app.use(cors())

const posts = [
    {
        username: 'Kyle',
        title: 'Post 1'
    },
    {
        username: 'Jim',
        title: 'Post 2'
    }
]

app.get('/', authenticateToken, (request, response) => {

    console.log("Kishore")

    // response.send(crypto.randomBytes(64).toString('hex'))
    response.json(posts.filter(post => post.username === request.user.name))
})

app.post('/', (request, response) => {
    
    const usernname = request.body.username

    const user = {
        name: usernname
    }

    const access_token = jwt.sign(user, process.env.ACCESS_TOKEN_SECRET)

    response.send({access_token})

})

function authenticateToken(request, response, next) {
    const authHeader = request.headers['authorization']
    const token = authHeader && authHeader.split(' ')[1]
    if (token === null) return response.sendStatus(401)

    jwt.verify(token, process.env.ACCESS_TOKEN_SECRET, (error, user) =>{
        if (error) return response.sendStatus(403)
        request.user = user
        next()
    })
}

app.listen(4000, {})

// require('crypto').randomBytes(64).toString('hex')