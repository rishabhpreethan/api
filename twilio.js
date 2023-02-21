const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;
const client = require('twilio')(accountSid,authToken);


// console.log("Starting program");
// client.messages
//     .list()
//     .then((messages) => messages.forEach(m => console.log(m.sid)))
//     .catch((err) => console.error(err));
// console.log("Gathering message log");

async function deleteAllMessages() {
    const messages = await client.messages.list();
    for (message of messages) {
        console.warn(`Deleted ${message.sid}`);
        message.remove();
    }
}

console.log("Starting program");
deleteAllMessages()
    .then(() => console.log("DONE"))
    .catch((err) => console.error(err));