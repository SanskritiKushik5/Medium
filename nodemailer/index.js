const express = require("express");
var nodemailer = require("nodemailer");
const dotenv = require("dotenv");
dotenv.config();

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set("view engine", "ejs");
app.set("views", __dirname + "/views");

app.get("/", (req, res) => {
    res.render("index");
});

app.post("/sendmail", async (req, res) => {
    const email = req.body.email;
    const name = req.body.name;
    const msg = req.body.msg;
    try {
        var transporter = nodemailer.createTransport({
            service: "gmail",
            auth: {
                user: process.env.GMAILID,
                pass: process.env.GMAILPASSWORD,
            },
        });

        var mailOptions = {
            from: process.env.GMAILID,
            to: email,
            subject: `New Mail from ${name}`,
            text: msg,
        };

        transporter.sendMail(mailOptions, function (error, info) {
            if (error) {
                console.log(error);
                res.redirect("/");
            } else {
                console.log("Email sent: " + info.response);
            }
        });
    } catch (e) {
        console.log(e);
    }
    res.redirect("/");
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log("Started on PORT: " + PORT));


