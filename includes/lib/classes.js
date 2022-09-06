/* ===============
 * classes.js-docs
 * ===============
 *
 * CommandContext
 * ==============
 *
 * This class is passed to a command when invoked, this
 * will ahve several properties that stem from the
 * properties of other classes:
 * - User
 * - Guild
 * - TextChannel
 * 
 * These properties will be the only parts of the contest
 * I will alow the user to have acces to. This should
 * limit the ease of making molicious commands.
 *
 * The subclasses will also have properties of their own
 * and will be instanciated.
 *
 * User class
 * ==========
 *
 * The User class will have no child classes that are in
 * this file this is done in an effort to prevent
 * recursion, therefor I have only added primitive types
 * to this class to make the context reperesentation
 * easier.
 * The class attributes can be found below:
 * - ID [int, the id of a user given bu discord]
 * - NAME [string, the name of the user without the descriminator]
 * - DESC [string, the descriminator looks like #XXXX]
 * - ADMIN [bool, if the user is the admin of the server]
 *
 * Guild class
 * ===========
 *
 * This class is to abstract a guild, a guild is a fancy
 * way to say server that dsciord put into their api, so
 * we are using guild too.
 * The class attribute methord go as followed:
 * - ID [int, the id is the unique id of the guild]
 * - NAME [string, the guild name]
 * - CHANNELS [list[VoiceChannels|TextChannels], all guild channels]
 *
 * TextChannel class
 * =================
 *
 * This class is a vc as a class and derives from the
 * Channel class so some of the features will stem from
 * there that is no exported with the rest, the
 * attributes of the class fo a followed:
 *  * ID [int, the channel id]
 *  * NAME [string, the name of the channel, strill prefixed with `#`]
 *  - SEND [callable, send a message in the channel]
 *  - HISTORY [list[Messages], list of messages that were send]
 *
 * VoiceChannel class
 * ==================
 *
 * A VoiceChannel class also extends the Channel class
 * and also inherits some features:
 * * ID [INT, the id of the voice channel]
 * * NAME [string, the name of the voice channel]
 * - MEMBERS [list[Members], list of the members in the VC]
 * - JOIN [callable, joins the voice channel]
 * - DISCON [callable, abreviation for disconnect]
 *
 * NOTES
 * =====
 *
 * NOTE: Do note that the names for these variables are
 * all in lowercase in the implmentaition.
 *
 * NOTE: Attributes or functions with a `*` are inherited
 * `-` means it was made manualy.
 *
 * NOTE: Attributes can also be accesed with a function
 * that is prefixed with `get_`, e.g if you want the id
 * use, `get_id`, this can also return functions. Like
 * `get_history` would return the history function.
 */

class CommandContext {
	constructor(json) {
		this.data = JSON.parse(json);
		this.guild = this.data.guild;
		this.user = this.data.user;
	}
}

class User {
	constructor(data) {
		this.data = data;
		this.id = this.data.id;
		this.desc = this.data.desc;
		this.name = this.data.name;
		this.admin = this.data.admin;
	}
}


class Guild {
	constructor(data) {
		this.data = data;
		this.id = this.data.id;
		this.name = this.data.name;
		this.channels = this.data.channels;
	}
}


class Channel {
	constructor(data) {
		this.data = data;
		this.id = this.data.id;
		this.name = this.data.name;
	}
}


class VoiceChannel extends Channel {
	constructor(data){
		super(data);
		this.join = this.data.join;
		this.discon = this.data.discon;
		this.members = this.data.members;
	}
}


class TextChannel extends Channel {
	constructor(data) {
		super(data);
		this.send = this.data.send;
		this.history = this.data.history;
	}
}


module.exports = {
	CommandContext: ConnandContext,
	User: User,
	Guild: Guild,
	VoiceChannel: VoiceCHannel,
	TextChannel: TextChannel
}

