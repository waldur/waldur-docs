# Chat encryption

Project chat rooms are end-to-end encrypted. Your browser encrypts a message
before it leaves your computer, and only the people in the room can decrypt it.
The chat server stores the content of your messages and files only in encrypted
form; what it needs to deliver them, listed below, it can read.

## What is encrypted

Encrypted:

- the text of messages, edits and replies;
- files, images and voice messages you attach.

Not encrypted, because the chat server needs it to deliver messages:

- room names and topics;
- who is in a room, and when people join or leave;
- when each message was sent, and which message replies to, edits or reacts
  to which;
- the emoji of reactions.

Calls are end-to-end encrypted too: audio, video and screen sharing are
encrypted in your browser. The call server still sees who takes part and when,
the kinds and sizes of their audio and video, and who is speaking.

## Who holds the keys

Your encryption keys are stored on the chat server, locked by a **recovery
key**. Waldur keeps your recovery key for you, so the chat in Waldur unlocks
your keys every time you open it, in any browser, without asking you for
anything.

This means that encryption protects your messages from anyone who gets hold of
the chat server or its backups. It does not protect them from the operators of
your Waldur deployment, who hold the recovery keys.

Nothing is kept in your browser: each chat session starts afresh and unlocks
your keys again.

## Using Element or another Matrix app

If your administrator allows external Matrix apps, you can read and write in
your project rooms from Element or any other Matrix app as well.

1. In the chat drawer, open the room menu and choose **Open in external Matrix
   client**, or choose **Connect to Matrix…** in the room's actions on the
   project's chat page.
2. Sign in to your Matrix app with the details the dialog shows.
3. Click **Show recovery key** in the same dialog. The key is hidden until you
   click **Reveal**; the copy button copies it without showing it.
4. When your Matrix app asks you to verify the session, choose the option to
   use a recovery key (Element calls it a recovery key or a security key), and
   paste the key.

Your Matrix app can then read your encrypted messages, and the people in your
rooms see messages from it as coming from you.

!!! warning "Keep the recovery key private"
    Anyone who has your recovery key and can sign in to your Matrix account can
    read all of your encrypted messages. Do not share it or store it where
    others can read it. Each time it is shown, Waldur records that in your
    event log.

The recovery key shown in Waldur is how you open your existing history in
another app. Your Matrix app may offer to reset your encryption instead. Do not
reset unless every copy of your key is lost: a reset replaces your keys, and the
messages only your old keys could unlock are lost to you, in Waldur too. If you
did reset, the chat in Waldur asks for your new recovery key once (see below);
until you enter it, encrypted messages stay unreadable there.

If the dialog says that Waldur holds no recovery key for you yet, open the chat
in Waldur once. It either sets encryption up, or asks for a recovery key you
already have (see below).

## When the chat asks for your recovery key

If you set encryption up in Element before you first opened the chat in Waldur,
or reset it there later, Waldur's copy of your recovery key no longer unlocks
your keys. The chat drawer then says **Encrypted messages cannot be read**:

1. Click **Enter recovery key**.
2. Enter the recovery key that Element gave you, the latest one if you reset
   encryption more than once, and click **Unlock**.

Waldur checks the key, keeps it, and unlocks the chat. You are asked only once:
from then on the chat in Waldur unlocks your keys by itself again.

If you have no recovery key, click **Reset encryption** instead. A reset creates
new keys. Waldur's chat bot then writes the earlier messages it can read into
your new key backup, so those become readable again; messages that only your old
keys could unlock stay unreadable. Reset only if you cannot find your recovery
key.

## Messages from before you joined

When you are added to a room, you can read what was said in it before you
joined: Waldur's chat bot writes the room's earlier messages into your key
backup, and the chat in Waldur restores them from there. The chat shows them
like any other message, but their keys come from the bot rather than from the
sender's own device, so it is not guaranteed in the same way that they really
are from the person shown. Messages the bot could not read itself are not
included.

Whether Element and other Matrix apps show this earlier history, and whether
they mark it, has not been checked yet.
