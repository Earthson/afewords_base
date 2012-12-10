;(function()
{

    SyntaxHighlighter = SyntaxHighlighter || (typeof require !== 'undefined'? require('shCore').SyntaxHighlighter : null);
    
    function Brush()
    {
        var datatypes = 'int';
        var keywords = 'break default func interface select'+
                        'case defer go map struct'+
                        'chan else goto package switch'+
                        'const fallthrough if range type'+
                        'continue for import return var';
						
        this.regexList = [
            { regex: SyntaxHighlighter.regexLib.singleLineCComments,	css: 'comments' },		// one line comments
            { regex: /\/\*([^\*][\s\S]*)?\*\//gm,						css: 'comments' },	 	// multiline comments
            //{ regex: /\/\*(?!\*\/)\*[\s\S]*?\*\//gm,					css: 'preprocessor' },	// documentation comments
            { regex: SyntaxHighlighter.regexLib.doubleQuotedString,		css: 'string' },		// strings
            { regex: SyntaxHighlighter.regexLib.singleQuotedString,		css: 'string' },		// strings
            { regex: /\b([\d]+(\.[\d]+)?|0x[a-f0-9]+)\b/gi,				css: 'value' },			// numbers
            //{ regex: /(?!\@interface\b)\@[\$\w]+\b/g,					css: 'color1' },		// annotation @anno
            //{ regex: /\@interface\b/g,									css: 'color2' },		// @interface keyword
            { regex: new RegExp(this.getKeywords(datatypes), 'gm'),		css: 'color1 bold' },
            { regex: new RegExp(this.getKeywords(keywords), 'gm'),		css: 'keyword' }		// go keyword
        ];

        this.forHtmlScript({
            left	: /(&lt;|<)%[@!=]?/g, 
            right	: /%(&gt;|>)/g 
        });
    };

    Brush.prototype	= new SyntaxHighlighter.Highlighter();
    Brush.aliases	= ['go'];

    SyntaxHighlighter.brushes.Go = Brush;

    typeof(exports) != 'undefined' ? exports.Brush = Brush : null;
})();